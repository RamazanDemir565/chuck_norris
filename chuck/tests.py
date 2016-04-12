from django.test import TestCase

# Create your tests here.
 <form method='POST'>
    {{form1.as_p}}
    <button type="submit" name="btnform1">Save Changes</button>
    </form>
    <form method='POST'>
    {{form2.as_p}}
    <button type="submit" name="btnform2">Save Changes</button>
    </form>