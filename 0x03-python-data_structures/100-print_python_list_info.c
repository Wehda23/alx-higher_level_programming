#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p){
	PyListObject *list = (PyListObject *)p;
	long int size = PyList_Size(list);
	Py_ssize_t index = 0;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	
	for (index = 0; index < size; index++)
	{
		printf("Element %ld: %s\n", index, Py_TYPE(PyList_GetItem(p, index))->tp_name);
	}
	
}
