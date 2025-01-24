select it.item_id, ii.item_name, ii.rarity
from item_tree it
join item_info ii
on it.item_id = ii.item_id
where it.parent_item_id in (select item_id from item_info where rarity='RARE')
order by it.item_id desc;
