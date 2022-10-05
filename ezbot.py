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
        g.add_cog_command(group, "welcome", "Sends a welcome message", "", """await interaction.response.send_message(\"Welcome to EZBot!\")""")
    if group == "SampleCommandGroup2":
        g.add_cog_command(group, "greet", "Sends Hello, followed by your name!", ["name: str"], """await interaction.response.send_message(\"Hello,  \" + name + \"!\")""")
    if group == "SampleCommandGroup3":
        g.add_cog_command(group, "fullgreet", "Sends Hello, followed by your name and age", ["name: str", "age: int"], """await interaction.response.send_message(\"Hello, \" + name + \", I believe you are \" + str(age) + \" years old!\")""")
    g.close_cog(group, "1026505045501554730")