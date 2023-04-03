take_off_checklist = ["Put on suit", "Seal hatch", "Check cabin pressure", "Fasten seatbelt",
                      "Tell Mission Control when checks are complete"]
spacewalk_checklist = ["Put on suit", "Check oxygen", "Seal helmet", "Test radio",
                       "Open airlock"]
pr_list = ["Taking a selfie", "Delivering lectures", "Doing TV interviews",
           "Meeting the public"]
rocket_landing_checklist = ["Aim trajectory course", "Activate slowing thrusters",
                            "Strap on seatbelts", "Clear FOD", "Tell Mission Control we landed"]
docking_checklist = ["Doors to manual", "Rotational lock-on", "Approach and lock"]
flight_manual = [take_off_checklist, spacewalk_checklist, docking_checklist, rocket_landing_checklist, pr_list]
x = 0
for i in pr_list[x]:
    print(flight_manual[x])
    x = x + 1
