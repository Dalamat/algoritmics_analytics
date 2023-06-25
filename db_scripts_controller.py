from db_scripts.refresh_db_events_check_errors import refresh_db_events
from db_scripts.refresh_db_groups_check_errors import refresh_db_groups
from db_scripts.refresh_db_invoices_check_errors import refresh_db_invoices
from db_scripts.refresh_db_students_check_errors import refresh_db_students
from db_scripts.update_db_events_check_errors import update_db_events
from db_scripts.update_db_invoices_check_errors import update_db_invocies
from db_scripts.update_db_students_check_errors import update_db_students
from db_scripts.refresh_db_leads import refresh_db_leads

SCRIPT_FUNCTIONS = {
    "refresh_db_events": refresh_db_events,
    "refresh_db_groups": refresh_db_groups,
    "refresh_db_invoices": refresh_db_invoices,
    "refresh_db_students": refresh_db_students,
    "update_db_events": update_db_events,
    "update_db_invocies": update_db_invocies,
    "update_db_students": update_db_students,
    "refresh_db_leads": refresh_db_leads
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