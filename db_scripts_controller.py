from db_scripts.refresh_db_events import refresh_db_events
from db_scripts.refresh_db_groups import refresh_db_groups
from db_scripts.refresh_db_invoices import refresh_db_invoices
from db_scripts.refresh_db_students import refresh_db_students
from db_scripts.update_db_events import update_db_events
from db_scripts.update_db_invoices import update_db_invocies
from db_scripts.update_db_students import update_db_students
from db_scripts.refresh_db_leads import refresh_db_leads
from db_scripts.refresh_db_budgets import refresh_db_budgets
from db_scripts.refresh_db_payments import refresh_db_payments

SCRIPT_FUNCTIONS = {
    "refresh_db_events": refresh_db_events,
    "refresh_db_groups": refresh_db_groups,
    "refresh_db_invoices": refresh_db_invoices,
    "refresh_db_students": refresh_db_students,
    "update_db_events": update_db_events,
    "update_db_invocies": update_db_invocies,
    "update_db_students": update_db_students,
    "refresh_db_leads": refresh_db_leads,
    "refresh_db_budgets": refresh_db_budgets,
    "refresh_db_payments" : refresh_db_payments
}

def db_scripts(script_function):
    function = SCRIPT_FUNCTIONS.get(script_function)
    
    if function is None:
        print("Script not found")
        return False

    return function() is True

# Test runs
# db_scripts("refresh_db_events")
# db_scripts("refresh_db_groups")
# db_scripts("refresh_db_invoices")
# db_scripts("refresh_db_students")
# db_scripts("update_db_events")
# db_scripts("update_db_invocies")
# db_scripts("update_db_students")
# db_scripts("refresh_db_leads")
# db_scripts("refresh_db_budgets")
# db_scripts("refresh_db_payments")