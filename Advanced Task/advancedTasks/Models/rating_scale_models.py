#rating Scale Models
class rating_scale:
    def __init__(self, name, description, score, label,score_description):
        self.name = name
        self.description = description
        self.score = score
        self.label = label
        self.score_description = score_description

class rating_status:
    def __init__(self, scale_name, status='pending'):
        self.scale_name = scale_name
        self.status = status

#ONB Models 
class ONB_Model:
    def __init__(self, id, listName, item):
        self.id = id
        self.listName = listName
        self.item = item

class ONB_Status:
    def __init__(self, ItemID, status='pending'):
        self.itemID = ItemID
        self.status = status

#task 10 to 13 model
class tab_Element_status:
    def __init__(self, tabElement, status='pending'):
        self.tabElement = tabElement
        self.status = status

class tab_elements:
    def __init__(self, identifier, default_label, label, enabled, description):
        self.identifier = identifier
        self.default_label =default_label
        self.label = label
        self.enabled = enabled
        self.description = description

class tab_permission:
    def __init__(self,identifier,  permission, role):
        self.identifier = identifier
        self.permission = permission
        self.role = role
