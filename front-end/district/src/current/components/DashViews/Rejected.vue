<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >

      <v-flex
        md12
      >

        <material-card 
        title="Previous Projects"
        color="black"
        >
        <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field><br>
          <v-spacer></v-spacer>
          <v-data-table
            :headers="headers"
            :items="items"
            :search="search"
            :rows-per-page-items="rowsPerPageItems"
            hide-actions
             row
             wrap
            class="elevation-1"
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text-general text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
             
              <td>{{ item.title }}</td>
                <td>{{ item.abstract }}</td>
                <td>{{ item.year }}</td>
              
            </template>
          </v-data-table>
        </material-card>
      </v-flex>

     
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    search: '',
    headers: [
     
      {
        sortable: true,
        text: 'Title',
        value: 'title'
      },
      
      {
        sortable: false,
        text: 'Abstract',
        value: 'abstract',
      },
      {
        sortable: false,
        text: 'Year',
        value: 'year',
      },
      
    ],
    items: []
        }),
        mounted() {
             axios.get("http://127.0.0.1:5000/filterprevioustopicbytitle").then(response => {
                this.items = response.data
                 //console.log(response)
            })
        }
}
</script>
