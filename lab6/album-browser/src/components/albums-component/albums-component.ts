import { Component, inject, OnInit, Signal } from '@angular/core';
import { AlbumButtonComponent } from '../album-button-component/album-button-component';
import { AlbumState } from '../../services/album-state';

@Component({
  selector: 'app-albums-component',
  imports: [AlbumButtonComponent],
  templateUrl: './albums-component.html',
  styleUrl: './albums-component.css',
})
export class AlbumsComponent implements OnInit {
  albumState = inject(AlbumState);


  ngOnInit(): void {
    this.albumState.refresh();
  }

  checkActualData(id: number): null | string {
    if (this.albumState.deletedIds().includes(id)) return null;
    console.log(Object.values(this.albumState.newTitles())[id]);
    return Object.values(this.albumState.newTitles())[id] ?? this.albumState.albumList().find(album => album.id === id)!.title;
  }

}
