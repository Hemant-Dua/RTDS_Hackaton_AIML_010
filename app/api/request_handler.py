from app.api.ai_classifier import classify_intent
from app.api.parameter_extractor import extract_parameters
from app.api.openstack_api import openstack_action
from app.api.confirmation_handler import ask_for_confirmation
from app.services.session_manager import start_session
from app.services.logger import log_request

async def process_query(user_query: str):
    # Step 1: Classify the intent
    intent, confidence = classify_intent(user_query)
    
    # Step 2: Extract parameters from the query
    params = extract_parameters(user_query)
    
    # Step 3: Log the request
    log_request(user_query, intent, params)
    
    # Step 4: Handle confirmation for destructive actions (e.g., delete VM)
    if intent in ["delete_vm", "resize_vm"]:
        confirmation = await ask_for_confirmation(user_query)
        if not confirmation:
            return {"status": "Aborted", "message": "Action cancelled by user."}
    
    # Step 5: Perform the action via OpenStack API
    result = await openstack_action(intent, params)
    
    # Step 6: Start session for multi-turn actions
    session_id = start_session(intent, params)
    
    return {"intent": intent, "result": result, "session_id": session_id}
