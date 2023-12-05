#include <stdio.h>

struct timespec;

#include <Python.h>
#include <time.h>

/**
 * print_python_list_info - is function prints info about python list
 * @p: object
 * Return: void nothing.
 */
void print_python_list_info(PyObject *p)
{
	long int size, index = 0, allocations;
	PyObject *obj;

	size = PyList_Size(p);
	allocations = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocations);

	for (index = 0; index < size; index++)
	{	obj = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(obj)->tp_name);
	}	
}
