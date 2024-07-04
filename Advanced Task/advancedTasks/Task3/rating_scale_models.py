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


