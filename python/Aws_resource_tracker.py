def active_stat(resources):
     resource_list= []
     for resource in resources:
       new_status = resource["status"]
       if new_status == "running":
          resource_list.append(resource)
     return resource_list

def monthly_cost(resources):
     total = 0
     for resource in resources:
       new_cost = resource["monthly_cost"]
       cost = int(new_cost[1:])
       total += cost
     return total

def most_expensive(resources):
    return max(resources, key=lambda r: int(r["monthly_cost"][1:]))

def group_resource(resources):
     region_counts = {}
     for resource in resources:
       region = resource["region"]
       if region in region_counts:
          region_counts[region] += 1
       else:
          region_counts[region] = 1
     return region_counts

resource1 = {"resource_type":"EC2",
             "name":"apa_instance",
             "region":"us-east1",
             "status": "running",
             "monthly_cost":"$700" }

resource2 = {"resource_type":"RDS",
             "name":"apa_database",
             "region":"us-east1",
             "status": "running",
             "monthly_cost":"$300" }

resource3 = {"resource_type":"S3",
             "name":"lama_storage",
             "region":"us-south1",
             "status": "running",
             "monthly_cost":"$500" }

resource4 = {"resource_type":"RDS",
             "name":"apa_instance",
             "region":"us-west1",
             "status": "stopped",
             "monthly_cost":"$500" }

resource5 = {"resource_type":"EC2",
             "name":"apa_database",
             "region":"us-east1",
             "status": "running",
             "monthly_cost":"$600" }

resource5 = {"resource_type":"S3",
             "name":"apa_storage",
             "region":"us-west1",
             "status": "stopped",
             "monthly_cost":"$100" }

resources = [resource1, resource2, resource3, resource4, resource5]
print("active resource include: ")
for resource in active_stat(resources):
  print(resource)
  print("......")
print(f"the total monthly cost is: ${monthly_cost(resources)}")

print(f"the most expexive service is: {most_expensive(resources)}")

print(group_resource(resources))
