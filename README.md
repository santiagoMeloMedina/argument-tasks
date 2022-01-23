## ArgumentTasks

This library helps you to call easily defined tasks for your project, all you need to do is create a `file` for your tasks and a `yml` with their description.

#### Example

1. Let's say you want to create a task for your project that welcomes people to your app, in this case, 'ArgumentTasks lib'. To do that you need to import `Interface` class from the library and instantiate it as follows:

```py
from argument_tasks import Interface
from example_data import methods

SOURCE_YML_FILE = open("example_data/tasks.yml", "r")

Interface(SOURCE_YML_FILE, methods).run()
```

As you can see, we have defined a folder `example_data` that contains a `yml` file where the tasks are defined, and a `methods` file where the task's code is defined. Finally, the output for the code above is the text the `hello_arg` method from the methods file is printing.

```
Hello from ArgumentTasks lib!
```

Now, the methods defined are normal functions that must contain the parameter `**kwargs`. Bellow is the `methods` file code imported in the example.

```py
def hello_arg(**kwargs):
    print("Hello from ArgumentTasks lib!")
```

There's also a necessary `yml` file in the example called **tasks.yml** where the tasks are defined. Below is the file code used in the example.

```yml
hello:
  action: hello_arg
  values: []
```

As you can see the file has a certain structure, here is an example of it.

```yml
<command_name: str>:
    action: <method_name: str>
    values:
        -
            name: <arg_name: str>
            type: <arg_type: python_class>
            required: <whether_arg_is_required: bool>
            description: <arg_description: str>
```

Cheers 👍