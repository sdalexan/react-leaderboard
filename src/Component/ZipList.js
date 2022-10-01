import React , {Component} from 'react';
import service from '../Services/service';
import DataTable from 'react-data-table-component';

const columns = [
    {
        name: "Postal Code",
        selector: 'postal_code',
        center:true,
      },
      {
        name: 'Price Change',
        selector: 'change_price',
        sortable: true,
        center:true,
    },
      {
        name: 'Current Price',
        selector: 'current_price',
        sortable: true,
        center:true,
    },
  ];


class ZipList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };
      }


      componentDidMount() {
        this.getData();
        this.interval = setInterval(() => {
            localStorage.clear();
            this.getData();
        }, process.env.REACT_APP_REFRESH_RATE);
    }


    async getData() {
        const data = await service('../data/data_zip.json');
        this.setState({
            data: data.map((state, index) => ({
                rank : index + 1 , 
                postal_code : state.name,
                change_price: (100 * Number(state.median_listing_price_mm).toLocaleString('en')).toFixed(2) + "%",
                current_price: "$" + Number(state.median_listing_price).toLocaleString('en'),

            }))
        });
    }


     componentWillUnmount() {
       clearInterval(this.interval);
     }

     render(){
        return (
            <div className="list-container">
                <h2>Zip Codes with Highest Monthly Price Drop</h2>
                <DataTable
                    columns={columns}
                    highlightOnHover
                    pointerOnHover
                    striped
                    className="list-table"
                    data={this.state.data}
                />
            </div>
    );
}}


export default ZipList;
