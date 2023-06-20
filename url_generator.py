from datetime import datetime, timedelta

# Get the current date and the date last_days days ago
end_date = datetime.now().strftime('%Y-%m-%d')
last_days = 7 #Number of days before the current date to be donwloaded
start_date = (datetime.now() - timedelta(days=last_days)).strftime('%Y-%m-%d')

# Construct the URL with dynamic dates
bo_csv_url_invoices_filter = f"https://backoffice.algoritmika.org/payment/manage/invoices?InvoiceWithPaymentSearch%5BpaymentUpdatedAt%5D={start_date}+-+{end_date}&InvoiceWithPaymentSearch%5BpaymentUpdatedAtStart%5D={start_date}&InvoiceWithPaymentSearch%5BpaymentUpdatedAtEnd%5D={end_date}&export=true&name=default&exportType=csv"

bo_csv_url_students_filter = f"https://backoffice.algoritmika.org/student?StudentSearch%5Bid%5D=&StudentSearch%5Bupdated_at%5D={start_date}%20-%20{end_date}&export=true&name=default&exportType=csv"


# Output the URL
#print(bo_csv_url_invoices_filter, bo_csv_url_students_filter)