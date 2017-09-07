

Ravin_visited = set("""Madagascar
Canada
Japan
Brunei
Hong Kong
Russia
Azerbaijan
""".split("\n"))


Polina_visited = set("""Germany
France
United Kingdom
Austria
Canada
Azerbaijan
Ukraine""".split("\n"))

#remember to venn diagram this as a set!!!


print("Both Visited:", Ravin_visited & Polina_visited)
print("Either or visited:", Ravin_visited | Polina_visited)
print("Just One visited:", Ravin_visited ^ Polina_visited)
print("Just Ravin:", Ravin_visited - Polina_visited)
print("Just Polina:", Polina_visited - Ravin_visited)

#Results
#Both Visited: {'Canada', 'Azerbaijan'}
#Either or visited: {'', 'France', 'Brunei', 'Canada', 'Japan', 'Russia', 'Ukraine', 'Hong Kong', 'Azerbaijan', 'Austria', 'Germany', 'United Kingdom', 'Madagascar'}
#Just One visited: {'', 'Brunei', 'Japan', 'Hong Kong', 'Germany', 'Madagascar', 'France', 'Russia', 'Ukraine', 'Austria', 'United Kingdom'}
#Just Ravin: {'', 'Brunei', 'Japan', 'Russia', 'Hong Kong', 'Madagascar'}
#Just Polina: {'France', 'United Kingdom', 'Austria', 'Germany', 'Ukraine'}
