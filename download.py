import sys
import login
import asyncio
from tqdm import tqdm
from script_executor import execute_script
import paths
from telegram_client import send_group_message

def download_file(session, url, output_path, chunk_size=1024*1024):
    response = session.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        size_provided = total_size > 0
        progress = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", file=sys.stdout)
        with open(output_path, "wb") as f:
            try:
                for data in response.iter_content(chunk_size=chunk_size):
                    progress.update(len(data))
                    f.write(data)
            except Exception as e:
                progress.close()
                print("Error occurred while downloading the CSV file due to an exception:", e)
                return False
        progress.close()
        if size_provided and progress.n != progress.total:
            print("Error occurred while downloading the CSV file.",progress.n,"!=",progress.total)
            return False
        else:
            print("CSV file downloaded successfully to", output_path)
            return True
    else:
        print("Error downloading the CSV file")
        return False
    
def download_and_update(csv_url, output_path, table_name, script_path):
    session = login.get_authenticated_session()
    if session:
        attempt = 1
        while attempt <= 5:
            if download_file(session,csv_url,output_path):
                print("Proceed to DB update")
                if execute_script(script_path):
                    asyncio.run(send_group_message(table_name+" "+"Updated*"))
                else:
                    asyncio.run(send_group_message(table_name+" "+"Script Failed*"))
                break
            else:
                print("Download failed")
                attempt += 1
        else:
            print("Download stopped")
            asyncio.run(send_group_message(table_name+" "+"Download Failed*"))
    session.close()