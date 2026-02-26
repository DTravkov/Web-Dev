import { Component, computed, inject, input } from '@angular/core';
import { Album } from '../../models/album';
import { Router } from '@angular/router';
import { AlbumState } from '../../services/album-state';

@Component({
  selector: 'app-album-button-component',
  imports: [],
  templateUrl: './album-button-component.html',
  styleUrl: './album-button-component.css',
})
export class AlbumButtonComponent {
  albumState = inject(AlbumState);
  router = inject(Router);

  albumData = input.required<Album>();

  goToAlbum() {
    const id = this.albumData().id;
    this.albumState.setPendingId(id);
    this.router.navigate(['/albums', id.toString()]);
  }
}
