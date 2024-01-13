from django.shortcuts import render ,redirect , HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def index(request):
    #Cart.objects.all().delete()
    #OrderMaster.objects.all().delete()
    #OrderDetail.objects.all().delete()
    return render (request,'order/index.html',{})



def hotel_login(request):
    if request.method == "POST":
        mb=request.POST ['mb']
        pin=request.POST ['pin']
        s= Hotel.objects.filter(mobile=mb,pin=pin,status=1)
        if s:
            request.session['hotel_mobile'] = request.POST["mb"]
            return redirect('hotel_dashboard')
        else:
            messages.success(request,"please insert correct information or call more suport 9730991252")            
            return redirect('hotel_login')
    return render(request,'order/hotel_login.html')



def marketing_employee_login(request):
    if request.method == "POST":
        mb=request.POST ['mb']
        pin=request.POST ['pin']
        s= Marketing_Employee.objects.filter(employee_mobile=mb,pin=pin,status=1)
        if s:
            request.session['marketing_employee_mobile'] = request.POST["mb"]
            return redirect('hotel')
        else:
            messages.success(request,"please insert correct information")            
            return redirect('marketing_employee_login')
    return render(request,'order/marketing_employee_login.html')



    




def employee(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        e=Employee.objects.filter(hotel_id=h.id)
        context={
            'h':h,
            'e':e
        }
        if request.method == "POST":
            if "Add" in request.POST:
                hotel_id=request.POST.get('hotel_id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                department=request.POST.get('department')
                #validatin
                if Employee.objects.filter(employee_mobile=employee_mobile).exists():
                    messages.success(request,"Employee Allready Exits")
                else:
                    Employee(
                        hotel_id=hotel_id,
                        employee_name=employee_name,
                        employee_address=employee_address,
                        employee_mobile=employee_mobile,
                        pin=pin,
                        department=department,
                        added_by=h.hotel_name,
                    ).save()
                    messages.success(request,"Employee Edit Succesfully") 
            elif "Edit" in request.POST:
                hotel_id=request.POST.get('hotel_id')
                id=request.POST.get('id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                department=request.POST.get('department')
                #print(id)
                Employee(
                    hotel_id=hotel_id,
                    id=id,
                    employee_name=employee_name,
                    employee_address=employee_address,
                    employee_mobile=employee_mobile,
                    pin=pin,
                    department=department,
                    added_by=h.hotel_name,
                ).save()
                messages.success(request,"Employee Edit Succesfully") 
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Employee.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Employee.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Employee.objects.get(id=id)
                ac.status='1'
                ac.save()                                                
        return render(request,'order/employee.html',context=context)
    else:   
        return redirect('hotel_login')



    
def dish_category(request):
    if request.session.has_key('hotel_mobile'):
        request.session.has_key('hotel_mobile')
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        dc=Dish_category.objects.filter(hotel_id=h.id)
        context={
            'dc':dc,
            'h':h,       
        }
        if request.method == "POST":
            if "Add" in request.POST:
                name=request.POST.get('name')
                hotel_id = request.POST.get('hotel_id')
                Dish_category.objects.create(
                    category_name=name,
                    hotel_id=hotel_id
                )
                messages.success(request,"Category Added Succesfully")
            elif "Edit" in request.POST:
                name=request.POST.get('name')
                id=request.POST.get('id')
                edit_category=Dish_category.objects.get(id=id)
                edit_category.category_name=name
                edit_category.save()
                messages.success(request,"Category Edit Successfully")
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Dish_category.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='1'
                ac.save()            
        return render(request,'order/dish_category.html',context=context)
    else:
        return redirect('hotel_login')

def dish(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        dc=Dish_category.objects.filter(hotel_id=h.id,status=1)
        d=Dish.objects.filter(hotel_id=h.id)
        context={
            'c':dc,
            'h':h,
            'd':d       
        }
        if "Add" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                hotel_id=hotel_id,

            ).save()
            messages.success(request,"Dish Added Succesfully")
        elif "Edit" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            dish_id=request.POST.get('dish_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                hotel_id=hotel_id,
                id=dish_id
            ).save()
            messages.success(request,"Dish Edit Succesfully")            
        elif "Delete" in request.POST:
            dish_id=request.POST.get('dish_id')
            Dish.objects.get(id=dish_id).delete()
            messages.success(request,"Dish Delete Successfully")
        elif "Active" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='0'
            ac.save()
        elif "Deactive" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='1'
            ac.save()            
        return render(request,'order/dish.html',context=context)
    else:
        return redirect('hotel_login')
    






    
def table(request):
    if request.session.has_key('hotel_mobile'):
        request.session.has_key('hotel_mobile')
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        t=Table.objects.filter(hotel_id=h.id)
        context={
            't':t,
            'h':h,       
        }
        if request.method == "POST":
            if "Add" in request.POST:
                
                t=Table.objects.filter(hotel_id=h.id).count()
                t+=1
                hotel_id = request.POST.get('hotel_id')
                Table(
                    table_number=t,
                    hotel_id=hotel_id
                ).save()
                messages.success(request,"Table Added Succesfully")
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Table.objects.get(id=id).delete()
                messages.success(request,"Table Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                ac=Table.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                ac=Table.objects.get(id=id)
                ac.status='1'
                ac.save()            
        return render(request,'order/table.html',context=context)
    else:
        return redirect('hotel_login')




def waiter_login(request):
    if request.method == "POST":
        mb=request.POST ['mb']
        pin=request.POST ['pin']
        s= Employee.objects.filter(employee_mobile=mb,pin=pin,status=1,department='waiter')
        if s:
            request.session['waiter_mobile'] = request.POST["mb"]
            return redirect('waiter_dashboard')
        else:
            messages.success(request,"please insert correct information or call more suport 9730991252")            
            return redirect('waiter_login')
    return render(request,'order/waiter_login.html')



def chef_login(request):
    if request.method == "POST":
        mb=request.POST ['mb']
        pin=request.POST ['pin']
        s= Employee.objects.filter(employee_mobile=mb,pin=pin,status=1,department='chef')
        if s:
            request.session['chef_mobile'] = request.POST["mb"]
            return redirect('chef_dashboard')
        else:
            messages.success(request,"please insert correct information or call more suport 9730991252")            
            return redirect('chef_login')
    return render(request,'order/chef_login.html')



def chef_dashboard(request):
    if request.session.has_key('chef_mobile'):
        cf = request.session['chef_mobile']
        e=Employee.objects.get(employee_mobile=cf)
        d=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=0)
        Accepted_dish=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=1,chef_id=e.id,status='Accepted')
        Delivered_dish=Cart.objects.filter(hotel_id=e.hotel_id,chef_id=e.id,status='Delivered')
        #print(e.id)
        context={
            'e':e,
            'd':d,
            'p':Accepted_dish,
            'Delivered_dish':Delivered_dish
        }   
        if "Accepted" in request.POST:
            id=request.POST.get('id')
            chef_id=request.POST.get('chef_id')
            if Cart.objects.filter(id=id).exists():           
                c=Cart.objects.get(id=id)
                c.chef_id=chef_id
                c.cook_status='1'
                c.status='Accepted'
                c.save()
            messages.success(request,"You Accepted this Dish for Processing")            
        elif "Delivered" in request.POST:
            id=request.POST.get('id')
            chef_id=request.POST.get('chef_id')
            if Cart.objects.filter(id=id).exists():  
                c=Cart.objects.get(id=id)
                c.chef_id=chef_id
                c.cook_status='1'
                c.status='Delivered'
                c.save()
            messages.success(request,"You Accepted this Dish for Processing") 
        return render(request,'order/chef_dashboard.html',context=context)
    else:
        return redirect('chef_login')







def waiter_dashboard (request):
    if request.session.has_key('waiter_mobile'):
        wm = request.session['waiter_mobile']
        w=Employee.objects.get(employee_mobile=wm) 
        t=Table.objects.filter(hotel_id=w.hotel_id,status=1)        
        context={
            'w':w,    
            't':t,
        }
        return render(request,'order/waiter_dashboard.html',context=context)
    else:
        return redirect('waiter_login')
    

def waiter_add_order(request,id):
    if request.session.has_key('waiter_mobile'):
        wm = request.session['waiter_mobile']
        w=Employee.objects.get(employee_mobile=wm)
        h=Hotel.objects.get(id=w.hotel_id)  
        dish_category=Dish_category.objects.filter(hotel_id=w.hotel_id,status=1)
        t=Table.objects.get(id=id)        
        cart=Cart.objects.filter(hotel_id=w.hotel_id,table_id=id)
        context={
            'w':w,    
            't':t,
            'dc':dish_category,
            'h':h,
            'cart':cart
        }
        if "Delete" in request.POST:
            cart_id=request.POST.get('cart_id')
            if Cart.objects.filter(id=cart_id).exists():
                Cart.objects.get(id=cart_id).delete()
        return render(request,'order/waiter_add_order.html',context=context)
    else:
        return redirect('waiter_login')
    
    



def dish_filter(request):
    if request.method == 'GET':
        filter_data = request.GET['filter']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_name__icontains=filter_data,hotel_id__icontains=hotel_id,status=1)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})



def filter_by_category(request):
    if request.method == 'GET':
        dish_category_id = request.GET['dish_category_id']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_category_id=dish_category_id,hotel_id=hotel_id,status=1)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})



def add_to_cart(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        table_id = request.GET['table_id']               
        dish_id = request.GET['dish_id']
        qty = request.GET['qty']
        price = request.GET['price']
        note = request.GET['note']
        table_number = request.GET['table_number']
        total_price = request.GET['total_price']
        d=Dish.objects.get(id=dish_id)
        Cart(
            dish_id=dish_id,
            dish_marathi_name=d.dish_marathi_name,
            hotel_id=hotel_id,
            table_id=table_id,            
            qty=qty,
            price=price,
            note=note,
            total_price=total_price,
            table_number=table_number
            ).save()
        cart=Cart.objects.values().filter(hotel_id=hotel_id,table_id=table_id)
        cart=list(cart)
        c=Cart.objects.filter(hotel_id=hotel_id,table_id=table_id)
        total_amount=0
        if c:
            for c in c:
                tempamount=(c.qty*c.price)
                total_amount+=tempamount
                print(total_amount)
        return JsonResponse({'status': 1,'cart':cart,'total_amount':total_amount})
    else:
        return JsonResponse({'status': 0})


def view_order(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        hotel=Hotel.objects.get(mobile=hm)
        dish_category=Dish_category.objects.filter(hotel_id=hotel.id,status=1)
        cart=Cart.objects.filter(hotel_id=hotel.id,table_id=id)
        table=Table.objects.get(id=id)
        amount=0
        if "Delete" in request.POST:
            cart_id=request.POST.get('cart_id')
            if Cart.objects.filter(id=cart_id).exists():
                Cart.objects.get(id=cart_id).delete()
        ct=Cart.objects.filter(hotel_id=hotel.id,table_id=id)
        if ct:
            for tb in ct:
                tempamount=(tb.qty*tb.price)
                amount+=tempamount
                print(amount)

        return render(request,'order/view_order.html',{'cart':cart,'table':table,'hotel':hotel,'dish_category':dish_category,'amount':amount})
    else:
        return redirect('hotel_login')




def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        processed_combinations = set()

        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            combination = (th_id, tbn)

            if combination not in processed_combinations:
                one_table = Table.objects.filter(hotel_id=th_id, table_number=tbn).first()
                if one_table:
                    send_table.append(one_table)
                    processed_combinations.add(combination)
                    print(one_table)

        data = {
            'all_table': send_table,
        }
        return render(request, 'order/hotel_dashboard.html', data)
    
    else:
        return redirect('hotel_login')
    



def running_table(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        table=Table.objects.filter(hotel_id=hotel_id)
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        processed_combinations = set()

        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            combination = (th_id, tbn)

            if combination not in processed_combinations:
                one_table = Table.objects.filter(hotel_id=th_id, table_number=tbn).first()
                if one_table:
                    send_table.append(one_table)
                    processed_combinations.add(combination)
                    #print(one_table)

        data = {
            'all_table': send_table,
            'table':table
        }
        return render(request, 'order/running_table.html', data)
    
    else:
        return redirect('hotel_login')

def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        return render(request, 'order/hotel_dashboard.html')
    else:
        return redirect('hotel_login')
    
def place_order(request,id):
    hotel_mobile = request.session['hotel_mobile']
    h=Hotel.objects.get(mobile=hotel_mobile)
    hotel_id=h.id
    f=OrderMaster.objects.filter(hotel_id=hotel_id).count()
    #print(f)
    f+=1
    amount=0
    c=Cart.objects.filter(hotel_id=hotel_id,table_id=id)
    for c in c:
        qty=c.qty
        price=c.price
        t=(qty*price)
        amount+=t
        table_number=c.table_number
        dish_name=c.dish.dish_name
        total_price=c.total_price
    OrderMaster(
        hotel_id=hotel_id,
        table_id=id,
        order_filter=f,
        total_price=amount
        ).save()
    cart=Cart.objects.filter(hotel_id=hotel_id,table_id=id)
    for cart in cart:
        qty=cart.qty
        price=cart.price
        table_number=cart.table_number
        dish_marathi_name=cart.dish.dish_marathi_name
        total_price=cart.total_price
        OrderDetail(
            hotel_id=hotel_id,
            table_number=table_number,
            dish_marathi_name=dish_marathi_name,
            qty=qty,price=price,
            total_price=total_price,
            order_filter=f
            ).save()
        Cart.objects.filter(hotel_id=hotel_id,table_id=id).delete()
    return redirect(f'/merge_card/{id}/{hotel_id}')




def merge_card(request,table_id,hotel_id):
    cart_item=Cart.objects.filter(hotel_id=hotel_id,table_id=table_id).exists()
    if cart_item == False:
        












def complate_order(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        hotel_id=h.id
        m=OrderMaster.objects.filter(hotel_id=hotel_id).order_by('-order_filter')
        context={
            'm':m
        }
        return render(request, 'order/complate_order.html',context)
    else:
        return redirect('hotel_login')
    









def complate_view_order(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hm)
        hotel_id=h.id
        od=OrderDetail.objects.filter(hotel_id=hotel_id,order_filter=id)
        total=0
        for t in od:
            total += (t.price*t.qty)
            table_number=t.table_number
            date=t.ordered_date
            bill_number=t.order_filter
        context={
            'h':h,
            'od':od,
            'total':total,
            'table_number':table_number,
            'date':date,
            'bill_number':bill_number
        }
        return render(request,'order/complate_view_order.html',context)
    else:
        return redirect('hotel_login')
    




def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["mb"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 10000 :
            request.session['sunil_mobile'] = s
            return redirect('marketing_employee')
        else:
            return redirect('sunil_login')
    return render(request,'order/sunil_login.html')

def marketing_employee(request):
    if request.session.has_key('sunil_mobile'):
        e=Marketing_Employee.objects.all()
        context={
            'e':e
        }
        if request.method == "POST":
            if "Add" in request.POST:
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                #validatin
                if Marketing_Employee.objects.filter(employee_mobile=employee_mobile).exists():
                    messages.success(request,"Employee Allready Exits")
                else:
                    Marketing_Employee(
                        employee_name=employee_name,
                        employee_address=employee_address,
                        employee_mobile=employee_mobile,
                        pin=pin,
                    ).save()
                    messages.success(request,"Employee Edit Succesfully") 
            elif "Edit" in request.POST:
                id=request.POST.get('id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                #print(id)
                Marketing_Employee(
                    id=id,
                    employee_name=employee_name,
                    employee_address=employee_address,
                    employee_mobile=employee_mobile,
                    pin=pin,
                ).save()
                messages.success(request,"Employee Edit Succesfully") 
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Marketing_Employee.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Marketing_Employee.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Marketing_Employee.objects.get(id=id)
                ac.status='1'
                ac.save()                                                
        return render(request,'order/marketing_employee.html',context)
    else:   
        return redirect('sunil_login')





def hotel (request):
    if request.session.has_key('marketing_employee_mobile'):
        mk = request.session['marketing_employee_mobile']
        m=Marketing_Employee.objects.get(employee_mobile=mk) 
        marketing_employee_id=m.id
        h=Hotel.objects.filter(marketing_employee_id=marketing_employee_id)
        context={
            'm':m,    
            'marketing_employee_id':marketing_employee_id,
            'h':h
        }
        if request.method == "POST":
            if "Add" in request.POST:
                marketing_employee_id=request.POST.get('employee_id')
                hotel_name=request.POST.get('hotel_name')
                owner_name=request.POST.get('owner_name')
                hotel_address=request.POST.get('hotel_address')
                mobile=request.POST.get('mobile')
                pin=request.POST.get('pin')
                #validatin
                if Hotel.objects.filter(mobile=mobile).exists():
                    messages.success(request,"Hotel Allready Exits")
                else:
                    Hotel(
                        marketing_employee_id=marketing_employee_id,
                        hotel_name=hotel_name,
                        owner_name=owner_name,
                        hotel_address=hotel_address,
                        mobile=mobile,
                        pin=pin
                    ).save()
            elif "Edit" in request.POST:
                marketing_employee_id=request.POST.get('employee_id')
                hotel_name=request.POST.get('hotel_name')
                owner_name=request.POST.get('owner_name')
                hotel_address=request.POST.get('hotel_address')
                mobile=request.POST.get('mobile')
                pin=request.POST.get('pin')
                hotel_id=request.POST.get('hotel_id')
                Hotel(
                    marketing_employee_id=marketing_employee_id,
                    hotel_name=hotel_name,
                    owner_name=owner_name,
                    hotel_address=hotel_address,
                    mobile=mobile,
                    pin=pin,
                    id=hotel_id                
                    ).save()
                messages.success(request,"Hotel Edit Succesfully") 
        return render(request,'order/hotel.html',context=context)
    else:
        return redirect('marketing_employee_login')
    

def remove_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        if Cart.objects.filter(id=id).exists():
                Cart.objects.get(id=id).delete()
        return JsonResponse({'status': 1,})
    else:
        return JsonResponse({'status': 0})











    
def test(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        hotel=Hotel.objects.get(mobile=hm)
        dish_category=Dish_category.objects.filter(hotel_id=hotel.id,status=1)
        table=Table.objects.get(id=id)
        print(table.id)
        cart=Cart.objects.filter(hotel_id=hotel.id,table_id=id)
        amount=0
       
  

               
        return render(request,'order/view_order.html',{'table':table,'cart':cart,'hotel':hotel})
    else:
        return redirect('hotel_login')


