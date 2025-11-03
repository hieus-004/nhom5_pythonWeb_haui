from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  
def update_cart_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get('product_id')
        change = int(data.get('change', 0))

        # Get user cart
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'error': 'Not logged in'})

        from web.models import TaiKhoan, GioHang, GioHang_SanPham, SanPham

        tai_khoan = TaiKhoan.objects.get(MaTK=user_id)
        gio_hang, _ = GioHang.objects.get_or_create(TaiKhoan=tai_khoan)
        try:
            cart_item = GioHang_SanPham.objects.get(GioHang=gio_hang, SanPham_id=product_id)
            cart_item.SoLuong = max(1, cart_item.SoLuong + change)  # Prevent quantity < 1
            cart_item.save()
        except GioHang_SanPham.DoesNotExist:
            if change > 0:
                cart_item = GioHang_SanPham.objects.create(
                    GioHang=gio_hang,
                    SanPham_id=product_id,
                    SoLuong=1
                )
            else:
                return JsonResponse({'success': False, 'error': 'Item not in cart'})

        return JsonResponse({'success': True, 'new_quantity': cart_item.SoLuong})

    return JsonResponse({'success': False, 'error': 'Invalid request'})