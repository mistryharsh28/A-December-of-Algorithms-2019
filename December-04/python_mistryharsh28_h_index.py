
def h_index(N, citations):

    citations = sorted(citations, reverse=True)

    h_index = None

    for index, citation in enumerate(citations):

        if((index + 1) == citation):
            h_index = citation 
            break
    
    return h_index

result = h_index(5, [4,3,0,1,5])
print(result)

result = h_index(6, [4,5,2,0,6,4])
print(result)