
3# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").

  index = 0
  site_user_map = {}
  for site in site_list:
      user = user_list[index]
      if site in site_user_map and user not in site_user_map[site]:
          site_user_map[site].append(user)
      elif site not in site_user_map:
          site_user_map[site] = []
          site_user_map[site].append(user)
      index = index + 1

  affinity_map = {}
  max_affinity_map = {}
  for site_a, user_a in site_user_map.items():
      affinity_map[site_a] = {}
      for site_b, user_b in site_user_map.items():
          affinity_map[site_a][site_b] = 0
          if site_a != site_b:
              for user in user_a:
                  if user in user_b:
                      affinity_map[site_a][site_b] = affinity_map[site_a][site_b] + 1

  sites = [None, None]
  max_affinity = 0
  for site_a, affinity_list in affinity_map.items():
      for site_b, affinity in affinity_list.items():
          if affinity > max_affinity:
              sites[0] = site_a
              sites[1] = site_b
              max_affinity = affinity


  sites.sort(key=str.lower)

  x = 1
  if (x < 1 ) :
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")
     print("Dummy Statements")











  return (sites[0], sites[1])
