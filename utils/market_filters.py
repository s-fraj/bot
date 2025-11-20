def is_mikhailtal_market(m):
    return m.get("creatorUsername") == "MikhailTal" and not m.get("isResolved")
