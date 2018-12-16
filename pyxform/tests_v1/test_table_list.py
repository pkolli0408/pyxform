from pyxform.tests_v1.pyxform_test_case import PyxformTestCase


MD = '''
| survey  |                    |            |       |                   |     
|         | type               | name       | label |appearance         |
|         | begin_group        | tablelist1 | Table |table-list minimal |
|         | select_one yes_no  | options1a  | Q1    |                   |                             
|         | select_one yes_no  | options1b  | Q2    |                   |
|         | end_group          |            |       |                   |
| choices |                    |            |       |                   |
|         | list_name          | name       | label |                   |
|         | yes_no             | yes        | Yes   |                   |
|         | yes_no             | no         | No    |                   |
            """  # noqa
'''  # nopep8

XML_CONTAINS = '''
<group appearance="field-list minimal" 
'''.strip()  # nopep8


class AreaTest(PyxformTestCase):
    def test_area(self):
        self.assertPyxformXform(
            name="area",
            md=MD,
            xml__contains=[XML_CONTAINS],
            debug=True
        )

""" 
xls

begin group	happy_sad_table	Table with image labels (made using an easier method)	This is a user-defined hint for the 1st row							table-list minimal
select_multiple  happy_sad	happy_sad_brian	Brian	This is a user-defined hint for the 2nd row							
select_multiple happy_sad	happy_sad_michael	Michael	This is a user-defined hint for the 3rd row							
end group										


-------------

xml outappearance
    <group appearance="field-list minimal" ref="/table-list-appearance-mod/happy_sad_table">
      <input ref="/table-list-appearance-mod/happy_sad_table/generated_table_list_label_7">
        <label>Table with image labels (made using an easier method)</label>
        <hint>This is a user-defined hint for the 1st row</hint>
      </input>
      <select appearance="label" ref="/table-list-appearance-mod/happy_sad_table/reserved_name_for_field_list_labels_8">
        <label> </label>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/reserved_name_for_field_list_labels_8/happy:label')"/>
          <value>happy</value>
        </item>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/reserved_name_for_field_list_labels_8/sad:label')"/>
          <value>sad</value>
        </item>
      </select>
      <select appearance="list-nolabel" ref="/table-list-appearance-mod/happy_sad_table/happy_sad_brian">
        <label>Brian</label>
        <hint>This is a user-defined hint for the 2nd row</hint>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/happy_sad_brian/happy:label')"/>
          <value>happy</value>
        </item>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/happy_sad_brian/sad:label')"/>
          <value>sad</value>
        </item>
      </select>
      <select appearance="list-nolabel" ref="/table-list-appearance-mod/happy_sad_table/happy_sad_michael">
        <label>Michael</label>
        <hint>This is a user-defined hint for the 3rd row</hint>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/happy_sad_michael/happy:label')"/>
          <value>happy</value>
        </item>
        <item>
          <label ref="jr:itext('/table-list-appearance-mod/happy_sad_table/happy_sad_michael/sad:label')"/>
          <value>sad</value>
        </item>
      </select>
    </group>
"""