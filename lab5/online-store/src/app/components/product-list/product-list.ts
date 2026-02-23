import { Component, inject, output } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { Product } from '../../models/product.model';
import { StorageService } from '../../services/storage-service';
import { ProductService } from '../../services/product-service';
import { CategoryMenu } from '../category-menu/category-menu';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard, CategoryMenu],
  templateUrl: `./product-list.html`,
  styleUrl: `./product-list.css`,
})
export class ProductList {
  productService = inject(ProductService);
  storageService = inject(StorageService);

  productList = this.productService.getProductListSignal();

  filterProducts(filters: string[]) {
    this.productService.filterProducts(filters);
  }

  likeProduct(productInstance: Product) {
    this.productService.likeProduct(productInstance);
  }

  deleteProduct(productInstance: Product) {
    this.productService.deleteProduct(productInstance);
  }

}
