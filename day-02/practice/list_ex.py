clouds = list()

clouds.append("AWS")
clouds.append("AZURE")
clouds.append("IBM")
clouds.append("GCP")
clouds.append("UTHO")

for cloud in clouds:
    if cloud == "AWS":
        print(f"{cloud} Master Devops - most used")
    elif cloud == "AZURE" or cloud == "GCP":
        print(f"{cloud} TWS mein cover hoga")
    elif cloud == "UTHO":
        print(f"{cloud} Indian Cloud")
    else:
        print(f"{cloud} Nahi ho payega")




