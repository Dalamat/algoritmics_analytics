from datetime import datetime, timedelta
import paths

def get_urls(table):
    # Get the current date and the date last_days days ago
    end_date = datetime.now().strftime('%Y-%m-%d')
    last_days = 7 #Number of days before the current date to be donwloaded
    start_date = (datetime.now() - timedelta(days=last_days)).strftime('%Y-%m-%d')

    # Construct the URL with dynamic dates
    if table == "EVENTS FULL":
        url = paths.bo_csv_url_events
    elif table == "GROUPS FULL":
        url = paths.bo_csv_url_groups
    elif table == "INVOICES FULL":
        url = paths.bo_csv_url_invoices
    elif table == "STUDENTS FULL":
        url = paths.bo_csv_url_students
    elif table == "PAYMENTS FULL":
        url = paths.bo_csv_url_payments
    elif table == "EVENTS UPDATES":
        url = paths.bo_csv_url_events_filter
    elif table == "INVOICES UPDATES":
        url = f"https://backoffice.algoritmika.org/payment/manage/invoices?InvoiceWithPaymentSearch%5BpaymentUpdatedAt%5D={start_date}+-+{end_date}&InvoiceWithPaymentSearch%5BpaymentUpdatedAtStart%5D={start_date}&InvoiceWithPaymentSearch%5BpaymentUpdatedAtEnd%5D={end_date}&export=true&name=default&exportType=csv"
    elif table == "INVOICES UPDATES_2":
        url = f"https://backoffice.algoritmika.org/payment/manage/invoices?InvoiceWithPaymentSearch%5BinvoiceCreatedAt%5D={start_date}+-+{end_date}&InvoiceWithPaymentSearch%5BinvoiceCreatedAtStart%5D={start_date}&InvoiceWithPaymentSearch%5BinvoiceCreatedAtEnd%5D={end_date}&export=true&name=default&exportType=csv"
    elif table == "STUDENTS UPDATES":
        url = f"https://backoffice.algoritmika.org/student?StudentSearch%5Bid%5D=&StudentSearch%5Bupdated_at%5D={start_date}%20-%20{end_date}&export=true&name=default&exportType=csv"
    elif table == "PAYMENTS UPDATES":
        url = f"https://backoffice.algoritmika.org/payment/manage?PaymentSearch%5Bid%5D=&PaymentSearch%5Bcreated_at%5D=&PaymentSearch%5BpaymentCreatedAtStart%5D=&PaymentSearch%5BpaymentCreatedAtEnd%5D=&PaymentSearch%5Bupdated_at%5D={start_date}%20-%20{end_date}&PaymentSearch%5BpaymentUpdatedAtStart%5D={start_date}&PaymentSearch%5BpaymentUpdatedAtEnd%5D={end_date}&export=true&name=default&exportType=csv" 
    else:
        url = None
    return url

# print(get_urls("events_full"))
# print(get_urls("invoices_filter"))
# print(get_urls("students_filter"))
# print(get_urls("payments_filter"))