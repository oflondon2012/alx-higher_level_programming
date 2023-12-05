#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <Python.h>
/**
 * print_python_list_info - function that print some basic python info
 * @p: list of python
 */
void print_python_list_info(PyObject *p)
{
	int elist;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elist = 0; elist < Py_SIZE(p); elist++)
	printf("Element %d: %s\n", elist, Py_TYPE(PyList_GetItem(p, elist))->tp_name);
}
