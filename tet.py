class TodoList:
    todo = {}

    def add_task(self, name, description):
        self.todo[name] = description
        return f'The schedule of tasks contains : {self.todo}'

    def finish_task(self, name):
        self.todo.pop(name)
        return f'After successfully completing a task, the list contains  {self.todo} tasks'

    def show_todo_list(self):
        print(f'The remaining tasks are : {self.todo.keys()}')

    def required_client_details(self, task_name):
        if task_name not in self.todo:
            client_details = input('Mock up ready? (YES/NO) : ')
            if client_details == 'NO':
                print('My client is a jerk')
            else:
                if client_details == 'YES':
                    details = input('Mock up from client: ')
                    self.todo[task_name] = details
                    return self.todo
                else:
                    print('This is not an answer sir, please tell me YES or NOT')


task_for_me = TodoList()
print(task_for_me.add_task('analyze', 'user story'))
print(task_for_me.add_task('unit testing', ' focus on a single part of a whole application'))
print(task_for_me.add_task('integration testing', 'how parts of the application work together as a whole'))
print(task_for_me.finish_task('analyze'))
task_for_me.show_todo_list()
print(task_for_me.required_client_details('UAT'))
