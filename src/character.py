class CharacterOption:
    def __init__(self,name,description,prereq,ranks):
        self.name = name
        self.description = description
        self.prereq = prereq
        self.ranks = ranks
        self.max_rank = len(ranks)

class CharacterSheet:
    def __init__(self,name,description,character_options,attributes,perks,items,stats,status_effects):
        self.name = name
        self.description = description
        self.character_options = character_options
        self.attributes = attributes
        self.perks = perks
        self.items = items
        self.stats = stats
        self.status_effects = status_effects

class Character:
    def __init__(self,name,attributes,items,stats,status_effects):
        self.name = name
        self.attributes = attributes
        self.items = items
        self.stats = stats
        self.status_effects = status_effects

