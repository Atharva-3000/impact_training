# Multithreading Notes

This repository contains notes on multithreading in Python.

## Overview

Multithreading allows for the execution of multiple threads simultaneously, enabling concurrent execution of different parts of a program. Threads are lightweight processes that run within a program's process.

## About Multithreading

1. Functionality or logic that executes simultaneously with other parts of the program.
2. Defining functionality and logic as a thread by overriding the `run` method of the `thread` class.
3. The `thread` class, a pre-defined class in the threading model.
4. Executing threads using the `start` method of the `thread` class.
5. Additional information on multithreading.


# Scheduling

Among multiple threads, which thread has to start execution first, for how much time thread has to execute, after alloted time is over, which thread has to be continued for execution. This all comes udner scheduling.

1. Scheduling is based on scheduling algorithms and every OS is following dynamic scheduling algorithms so that, scheduling is highly dynamic.
2. For every `thread` one name0 is assigned to thread class.

# Thread Name

1. ython interpreter assigns one unique name to each and every thread.
2. We can get names of thread, by calling `getName()` method of thread class.
3. We can also assign our own names to threads by calling `setName()` method of thread class.

## Suspending the execution of thread
1. We can suspend the execution of thread temporarily by calling `sleep()` function and `join()` method.

`sleep()` is a predefined function which is defined in *time* module.
1. It suspends the execution of current thread untill specified time is over.

`join()` it is a predefined method which is defined in thread class.
1. It stops the execution of current thread untill specified thread execution is over

## Usage

Feel free to explore the notes and use them as a reference for understanding multithreading in Python.