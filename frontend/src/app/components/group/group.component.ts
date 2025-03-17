import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Group {
  id: number;
  first_name: string;
  email: string;
  nv: number;
}

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {
  groups: Group[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchGroups();
  }

  fetchGroups() {
    this.http.get<Group[]>('http://127.0.0.1:8000/groups').subscribe(
      (data) => {
        this.groups = data;
      },
      (error) => {
        console.error('Error fetching groups:', error);
      }
    );
  }
}
