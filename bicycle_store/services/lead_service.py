from bicycle_store.config.settings import get_default_lead_source


def apply_default_lead_source(lead_doc):
    """
    Rule:
    Leads created without source -> Source = Website (configurable)
    """
    if not lead_doc.source:
        lead_doc.source = get_default_lead_source()
