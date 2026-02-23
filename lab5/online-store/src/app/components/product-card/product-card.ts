import { Component, input, signal, OnInit, output, effect, computed, inject } from '@angular/core';
import { Product } from '../../models/product.model';
import { ProductService } from '../../services/product-service';

@Component({
  selector: 'app-product-card',
  imports: [],
  templateUrl: `./product-card.html`,
  styleUrl: `./product-card.css`,
})
export class ProductCard {
  product = input.required<Product>();

  productService = inject(ProductService);

  currentImageId = signal(0);

  likeTrigger = signal(0);
  likeCount = computed(() => {
    this.likeTrigger();
    return this.productService.getLikesInfo(this.product());
  })

  deleteClicked = output<Product>();
  likeClicked = output<Product>();


  onDeleteClicked() {
    this.deleteClicked.emit(this.product());
  }

  onLikeClicked() {
    this.likeClicked.emit(this.product());
    this.likeTrigger.update(value => value + 1);
  }

  changeImage() {
    this.currentImageId.update((oldValue) => {
      let newValue = oldValue + 1;
      newValue %= this.product().images.length;
      return newValue;
    });
  }


  getWhatsappRedirectUrl() {
    return "https://wa.me/?text=Check out this product: " + this.product().link;
  }


  secondaryImageId = 0;
  getUniqueId() {
    this.secondaryImageId += 1;
    return this.secondaryImageId;
  }

}
