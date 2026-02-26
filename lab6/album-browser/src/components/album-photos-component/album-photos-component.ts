import { Component, inject, OnInit, Signal, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumService } from '../../services/album-service';
import { Photo } from '../../models/photo';
import { toSignal } from '@angular/core/rxjs-interop';
import { AlbumState } from '../../services/album-state';

@Component({
  selector: 'app-album-photos-component',
  imports: [],
  templateUrl: './album-photos-component.html',
  styleUrl: './album-photos-component.css',
})
export class AlbumPhotosComponent implements OnInit {
  router = inject(Router);
  albumState = inject(AlbumState);
  route = inject(ActivatedRoute);

  id: number = parseInt(this.route.snapshot.paramMap.get('id')!);

  ngOnInit(): void {
    this.albumState.setPendingId(this.id);
  }

  goBack() {
    this.router.navigate(['/albums', this.id]);
  }

}
