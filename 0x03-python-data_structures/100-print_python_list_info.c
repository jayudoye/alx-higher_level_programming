#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = 0, i = 0;
	PyObject *obj;
	PyTypeObject *name;
	PyListObject *list_alloc;

	if (!(PyList_Check(p)))
		return;

	list_size = PyList_Size(p);
	list_alloc = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", (int)list_size);
	printf("[*] Allocated = %d\n", (int)list_alloc->allocated);
	while (i < list_size)
	{
		obj = PyList_GetItem(p, i);
		name = Py_TYPE(obj);
		printf("Element %d: %s\n", (int)i, name->tp_name);
		i++;
	}
}
