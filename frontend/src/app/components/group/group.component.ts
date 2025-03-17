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
  filteredGroups: Group[] = []; // ✅ This will store filtered results
  searchText: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchGroups();
  }

  fetchGroups() {
    this.http.get<Group[]>('http://127.0.0.1:8000/groups').subscribe(
      (data) => {
        this.groups = data;
        this.filteredGroups = data; // ✅ Initialize filteredGroups
      },
      (error) => {
        console.error('Error fetching groups:', error);
      }
    );
  }

  onSearchChange() {
    this.filteredGroups = this.groups.filter(group =>
      group.first_name.toLowerCase().includes(this.searchText.toLowerCase()) ||
      group.email.toLowerCase().includes(this.searchText.toLowerCase()) ||
      group.nv.toString().includes(this.searchText)
    );
  }
}
