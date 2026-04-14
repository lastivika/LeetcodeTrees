"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dict = {emp.id: emp for emp in employees}

        def dfs(empid):
            emp = emp_dict[empid]
            return emp.importance + sum(dfs(subemp) for subemp in emp.subordinates)
        return dfs(id)
 