import json

jsonmsg = json.dumps({'Stacker1': ['CAT 1', 'CAT 2'], 'Stacker2' : None, 'Stacker3' : None, 'Stacker4' : ['CAT 8', 'CAT 11'], 'Stacker5' : ['CAT 6'], 'Stacker6' : ['Other'], 'Stacker7' : ['Unknown'], 'Stacker8' : ['mixed']}, ensure_ascii=False)
print(jsonmsg)    

