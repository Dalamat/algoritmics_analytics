import sys
from tqdm import tqdm
from login_bo import create_or_load_session
from login_amo import create_session_and_url
from login_gcp import gcp_get_values
import csv
from log_config import logger

def download_file(url, output_path, source="BO", chunk_size=1024*1024):
    if source == "BO":
        session = create_or_load_session()
        download_url = url
    elif source == "AMO":
        session, download_url = create_session_and_url()
    elif source == "GCP":
            values = gcp_get_values()
            if values:
                with open(output_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(values)
                logger.info(f"Data downloaded successfully to {output_path}")
                return True
            else:
                logger.warning(f"Downloading failed. {output_path}")
                return False
    else:
        logger.error(f"Wrong source - {source}. Must be BO or AMO")
        return False
    if session:
        response = session.get(download_url, stream=True)
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
                    logger.warning(f"Err occurred while downloading the CSV file to {output_path} due to an exception: {e}")
                    return False
            progress.close()
            if size_provided and progress.n != progress.total:
                logger.warning(f"Err occurred while downloading the CSV file to {output_path}. {progress.n} != {progress.total}")
                return False
            else:
                logger.info(f"CSV file downloaded successfully to {output_path}")
                return True
        else:
                logger.warning(f"Failed to obtain a response for {output_path} in {source}")
                return False
    else:
        logger.warning(f"Failed to obtain a session for {source}")
        return False