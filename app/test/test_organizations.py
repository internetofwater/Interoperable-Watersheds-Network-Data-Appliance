import unittest
from app.factory import bootstrap_test_app, deconstruct_test_app

class OrganizationsAPITest(unittest.TestCase):

    def setUp(self):
        self.app = bootstrap_test_app()
        self.client = self.app.test_client()
        
    
    def tearDown(self):
        deconstruct_test_app(self.app)
        self.app = None
        self.client = None

    def test_get_all(self):
        result = self.client.get('/orgs/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    def test_get_one(self):
        result = self.client.get('/orgs/epa')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Not Found')

    def test_post(self):
        result = self.client.post('/orgs/', json={
            "organization_id": "string",
            "parent_organization_id": "string",
            "name": "string",
            "url": "string",
            "contact_name": "string",
            "contact_email": "string",
            "sos_url": "string"
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')
        result = self.client.get('orgs/string')
        self.assertEqual(result.status_code,200, msg='Expected 200 OK')
    
    def test_delete_one(self):
        result = self.client.delete('/orgs/epar10')
        self.assertEqual(result.status_code, 204, msg="Expected 204 Deleted")
        result = self.client.get('/orgs/epar10')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')
        result = self.client.delete('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')

    
    def test_put_one(self):
        result = self.client.put('/orgs/epa',json={"sos_url": 'wwww.biscuit.com'})
        self.assertEqual(result.status_code, 200, msg="Expected 200 OK")
        result = self.client.get('/orgs/epa')
        self.assertEqual(result.json['sos_url'], 'wwww.biscuit.com', msg="Expected updated altitude value to be wwww.biscuit.com")
        result = self.client.put('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Organization Not Found')
