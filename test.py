testsubjects = ['no0/2~1~0~7~2~2~5', 'no1/35~0~8~0~7~4~54', 'no2/44~1~3~4~6~6~40', 'no3/45~0~0~3~8~8~36', 'no4/73~0~4~5~2~0~20', 'no5/85~0~7~2~8~0~5', 'no6/34~1~8~4~8~6~48', 'no7/38~0~6~8~4~3~47', 'no8/86~0~6~7~4~8~-5', 'no9/88~1~2~7~3~1~1']
testsubjects_alpha = []
testsubjects_beta = []
for years in range(10):
    # Unpacking and Edit
    for a in range(len(testsubjects)):
        testsubjects_alpha.append(testsubjects[a].split("/"))
    for b in range(len(testsubjects_alpha)):
        testsubjects_beta.append(testsubjects_alpha[b][1].split("~"))
    for c in range(len(testsubjects_beta)):
        testsubjects_reader = testsubjects_beta[c][0]
        testsubjects_reader = str(int(testsubjects_reader) + 1)
        testsubjects_beta[c][0] = testsubjects_reader
    
    # Repacking and Production

    
    print(f"Year {years}")
    print(testsubjects_beta[0][0])
print(testsubjects_beta)