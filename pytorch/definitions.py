cands_per_variable = {
    'glob' : 1,
    'cpf' : 25,
    'npf' : 25,
    'vtx' : 5,
    #'pxl' : ,
}
vars_per_candidate = {
    'glob' : 15,
    'cpf' : 16,
    'npf' : 6,#8
    'vtx' : 12,#14
    #'pxl' : ,
}
defaults_per_variable = {
    'glob' : [0 for i in range(vars_per_candidate['glob'])],
    'cpf' : [0 for i in range(vars_per_candidate['cpf'])],
    'npf' : [0 for i in range(vars_per_candidate['npf'])],
    'vtx' : [0 for i in range(vars_per_candidate['vtx'])],
    #'pxl' : ,
}
integer_variables_by_candidate = {
    'glob' : [2,3,4,5,8,13,14],
    'cpf' : [12,13,14,15],
    'npf' : [2],
    'vtx' : [3],
    #'pxl' : ,
}
