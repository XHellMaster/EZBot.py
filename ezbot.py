from generatorutils import Generator as gen

command_groups = [
    "SampleCommandGroup1",
    "SampleCommandGroup2",
    "SampleCommandGroup3",
]

g = gen("EZBot", command_groups)
g.generateFiles("MTAyNjUwNDQzNDkzMjUyNzE2NA.GHN8gF.P8k8grbz0we-rhaPNZnEhGED5uQL4UGJdmXv8Y", "1026504434932527164", "1026505045501554730")

for group in command_groups:
    g.create_cog_base(group)
    if group == "SampleCommandGroup1":
        g.add_cog_command(group, "test1", "Sends test1", "", """await interaction.response.send_message(\"test1\")""")
    if group == "SampleCommandGroup2":
        g.add_cog_command(group, "test2", "Sends test2 followed by your message", ["message: str"], """await interaction.response.send_message(\"test2 \" + message)""")
    if group == "SampleCommandGroup3":
        g.add_cog_command(group, "test3", "Sends test3 followed by your name and age", ["name: str", "age: int"], """await interaction.response.send_message(\"test3 \" + name + \", \" + str(age))""")
    g.close_cog(group, "1026505045501554730")



