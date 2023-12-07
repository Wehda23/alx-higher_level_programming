#include <stdio.h>


struct timespec;

#include <Python.h>
#include <time.h>

/**
 *  print_python_list - function that prints a python list
 *  @p: is a pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	const char *typeName;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python List\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 *  print_python_bytes - functio that prints python bytes
 *  @p: is a poitner to a PyObject
 */
void print_python_bytes(PyObject *p)
{

	const char *str = ((PyBytesObject *)p)->ob_sval;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Python Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);
	printf("trying string: %s\n", str);

	printf("first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}
