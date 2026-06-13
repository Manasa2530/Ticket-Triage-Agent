def classify_ticket(ticket):
    text = (
        ticket.get("title", "") + " " +
        ticket.get("description", "")
    ).lower()

    category = "General"
    priority = "Low"
    reason = "General issue detected."

    # Authentication problems
    if "password" in text or "login" in text or "signin" in text:
        category = "Authentication"
        priority = "High"
        reason = "User is unable to access their account."

    # Billing problems
    elif "payment" in text or "refund" in text or "charge" in text:
        category = "Billing"
        priority = "Critical"
        reason = "Issue is related to payment or billing."

    # Technical problems
    elif "error" in text or "bug" in text or "crash" in text:
        category = "Technical"
        priority = "Medium"
        reason = "Technical error or software issue detected."

    # Account problems
    elif "account" in text or "profile" in text:
        category = "Account"
        priority = "Medium"
        reason = "Issue is related to account settings or profile."

    return {
        "category": category,
        "priority": priority,
        "reason": reason
    }