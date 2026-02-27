import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Album } from '../models/album';
import { Photo } from '../models/photo';
@Injectable({
  providedIn: 'root',
})
export class AlbumService {
  private httpClient = inject(HttpClient);
  private baseUrl = 'https://jsonplaceholder.typicode.com/';

  getAlbums(): Observable<Album[]> {
    const obs = this.httpClient.get<Album[]>(this.baseUrl + "albums");
    return obs;
  }

  getAlbum(id: number): Observable<Album> {
    const obs = this.httpClient.get<Album>(this.baseUrl + "albums/" + id.toString());
    return obs;
  }

  getPhotos(id: number): Observable<Photo[]> {
    const obs = this.httpClient.get<Photo[]>(this.baseUrl + "albums/" + id.toString() + "/photos");
    return obs;
  }

  updateAlbum(id: number, newAlbum: Album) {
    const obs = this.httpClient.patch<Photo[]>(this.baseUrl + "albums/" + id.toString(), JSON.stringify(newAlbum), { observe: 'response' });
    return obs;
  }

  deleteAlbum(id: number) {
    const obs = this.httpClient.delete<Photo[]>(this.baseUrl + "albums/" + id.toString(), { observe: 'response' });
    return obs;
  }

  getBaseUrl() {
    return this.baseUrl;
  }


}
