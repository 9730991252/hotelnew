from django.shortcuts import render ,redirect , HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def index(request):
    #Cart.objects.all().delete()
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
            messages.success(request,"please insert correct information")            
            return redirect('hotel_login')
    return render(request,'order/hotel_login.html')



        

    




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
        dc=Dish_category.objects.filter(hotel_id=h.id)
        d=Dish.objects.filter(hotel_id=h.id)
        context={
            'c':dc,
            'h':h,
            'd':d       
        }
        if "Add" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            Dish(
                dish_name=dish_name,
                dish_category_id=dish_category_id,
                price=price,
                hotel_id=hotel_id,

            ).save()
            messages.success(request,"Dish Added Succesfully")
        elif "Edit" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            dish_id=request.POST.get('dish_id')
            Dish(
                dish_name=dish_name,
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
            c=Cart.objects.get(id=id)
            c.chef_id=chef_id
            c.cook_status='1'
            c.status='Accepted'
            c.save()
            messages.success(request,"You Accepted this Dish for Processing")            
        elif "Delivered" in request.POST:
            id=request.POST.get('id')
            chef_id=request.POST.get('chef_id')
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
        t=Table.objects.filter(hotel_id=w.hotel_id)        
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
        dish_category=Dish_category.objects.filter(hotel_id=w.hotel_id)
        t=Table.objects.get(id=id)        
        cart=Cart.objects.filter(hotel_id=w.hotel_id,table_id=id)
        context={
            'w':w,    
            't':t,
            'dc':dish_category,
            'h':h,
            'cart':cart
        }
        return render(request,'order/waiter_add_order.html',context=context)
    else:
        return redirect('waiter_login')
    
    



def dish_filter(request):
    if request.method == 'GET':
        filter_data = request.GET['filter']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_name__icontains=filter_data,hotel_id__icontains=hotel_id)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})



def filter_by_category(request):
    if request.method == 'GET':
        dish_category_id = request.GET['dish_category_id']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_category_id=dish_category_id,hotel_id=hotel_id)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})



def add_to_cart(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        table_id = request.GET['table_id']
        employee_id = request.GET['employee_id']        
        dish_id = request.GET['dish_id']
        qty = request.GET['qty']
        price = request.GET['price']
        note = request.GET['note']
        table_number = request.GET['table_number']
        total_price = request.GET['total_price']
        Cart(
            dish_id=dish_id,
            hotel_id=hotel_id,
            table_id=table_id,
            employee_id=employee_id,
            qty=qty,
            price=price,
            note=note,
            total_price=total_price,
            table_number=table_number
            ).save()
        #print(note)
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def view_order(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hm)
        t=Cart.objects.filter(hotel_id=h.id,table_id=id)
        tb=Cart.objects.filter(hotel_id=h.id,table_id=id)
        amount=0
        for tb in tb:
            table_number=tb.table_number
            tempamount=(tb.qty*tb.price)
            amount+=tempamount
            #print(amount)
        context={
            'h':h,
            't':t,
            'table_number':table_number,
            'total_am':amount,
            'table_id':id
                }
        return render(request,'order/view_order.html',context=context)
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
    print(f)
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
        dish_name=cart.dish.dish_name
        total_price=cart.total_price
        OrderDetail(
            hotel_id=hotel_id,
            table_number=table_number,
            dish_name=dish_name,
            qty=qty,price=price,
            total_price=total_price,
            order_filter=f
            ).save()
        Cart.objects.filter(hotel_id=hotel_id,table_id=id).delete()
    return redirect('running_table')


def complate_order(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        hotel_id=h.id
        m=OrderMaster.objects.filter(hotel_id=hotel_id)
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
        context={
            'h':h,
            'od':od,
            'total':total,
            'table_number':table_number,
            'date':date
        }
        return render(request,'order/complate_view_order.html',context)
    else:
        return redirect('hotel_login')


