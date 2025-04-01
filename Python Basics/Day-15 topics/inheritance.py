class Hexa_project:
    def __init__(self, project_name="default"):
        self.project_name = project_name

    def display(self):
        print(self.project_name)

    def project_1(self):
        print("project-1")

    def project_2(self):
        print("project-2")

class Hex(Hexa_project):
    def __init__(self, new_name, project_name="default"):
        super().__init__(project_name)
        self.new_name = new_name

    def display_new(self):
        print(self.new_name, " ", self.project_name)

    def project_3(self):
        print("Project-3")

    def project_4(self):
        print("Project-4")

pro = Hex("project_new", "project_old")
pro.project_1()
pro.project_3()
pro.display()
pro.display_new()