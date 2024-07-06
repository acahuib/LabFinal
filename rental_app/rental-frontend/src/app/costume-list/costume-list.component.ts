// En costume-list.component.ts

import { Component, OnInit } from '@angular/core';
import { CostumeService } from '../services/costume.service';

@Component({
  selector: 'app-costume-list',
  templateUrl: './costume-list.component.html',
  styleUrls: ['./costume-list.component.css']
})
export class CostumeListComponent implements OnInit {
  costumes: any[];

  constructor(private costumeService: CostumeService) {}

  ngOnInit(): void {
    this.getCostumes();
  }

  getCostumes(): void {
    this.costumeService.getCostumes()
      .subscribe(costumes => {
        this.costumes = costumes;
      });
  }
}

