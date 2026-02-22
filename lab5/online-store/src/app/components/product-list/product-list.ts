import { Component, inject, input, output } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { PRODUCTS } from '../../../assets/products';
import { Product } from '../../models/product.model';
import { StorageService } from '../../services/storage-service';
import { ProductService } from '../../services/product-service';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard],
  templateUrl: `./product-list.html`,
  styleUrl: `./product-list.css`,
})
export class ProductList {
  productService = inject(ProductService);
  storageService = inject(StorageService);
  productsSignal = this.productService.filteredProductList;

  deleteProductForward = output<Product>();
  likeProductForward = output<Product>();

  onDeleteProductForward(productInstance: Product) {
    this.deleteProductForward.emit(productInstance);
  }

  onLikeProductForward(productInstance: Product) {
    this.likeProductForward.emit(productInstance);
  }

}
