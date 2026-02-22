import { computed, inject, Injectable, Signal, signal } from '@angular/core';
import { PRODUCTS } from '../../assets/products';
import { Product } from '../models/product.model';
import { StorageService } from './storage-service';
import { single } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProductService {

  storageService: StorageService = inject(StorageService);

  activeFilters = signal<string[]>([]);

  rawProductListSignal: Signal<Product[]> = this.storageService.getRawProductListSignal();

  productList = computed(() =>
    this.rawProductListSignal().filter(
      prod => this.activeFilters().every(filt => Object.values(prod.category).includes(filt)))
  );

  getProductListSignal() {
    return this.productList;
  }

  filterProducts(newFilters: string[]) {
    this.activeFilters.set(newFilters);
  }

  likeProduct(productInstance: Product) {
    const list = this.rawProductListSignal();

    const id = list.findIndex(prod => prod.id === productInstance.id);

    const entry = list[id];
    list[id] = { ...entry, likes: entry.likes + 1 };
    this.storageService.update(list);

  }

  getLikesInfo(productInstance: Product) {
    const list = this.rawProductListSignal();
    const id = list.findIndex(prod => prod.id === productInstance.id);
    return list[id].likes;
  }

  deleteProduct(productId: number) {
    this.storageService.update(
      this.productList().filter(prod => prod.id !== productId)
    );
  }





}

