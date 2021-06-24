




from django.http import response


class APIService:
    print("-----------------")
    def __init__(self, id , class_name, method):
        self.id = id
        self.class_name = class_name
        self.method = method 
    
        if self.method == 'PUT' :
            print("----------------")
            print("----------------",self.class_name)
            return  self.put(id, class_name,method)


    def put(id, class_name, method):

        print("---------------------------user objects")
        user_object=class_name.objects.filer_by(id=id)
        print("user of user",user_object)
        return {'is':'is'}

    def get(id):
        return response({'is':'is'})

    def delete(id):
        return  response({'delete':'delete'})

    def post(id):
        return  response({'delete':'delete'})






        

            
